
import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C
import uuid
import os,sys
import tempfile
import pdb


class ResultCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin
    """

    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        sys.stdout.write(json.dumps({host.name: result._result}, indent=4))

class AnsibleApi:
    def __init__(self,hosts):
        self.filename = "/tmp/{0}".format(uuid.uuid4())
        self.tmp = open(self.filename,'a')
        self.tmp.write(hosts)
        self.tmp.close()
        Options = namedtuple('Options',
                             ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check',
                              'diff'])
        # initialize needed objects
        self.loader = DataLoader()
        self.options = Options(connection='ssh', module_path=None, forks=100, become=None, become_method=None,
                          become_user=None,
                          check=False,
                          diff=False)
        self.passwords = dict(vault_pass='secret')
        self.inventory = InventoryManager(loader=self.loader, sources=self.filename)
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
        self.hosts = hosts

    def run_cmd(self, cmd):
        # Instantiate our ResultCallback for handling results as they come in
        results_callback = ResultCallback()
        # create inventory and pass to var manager
        # use path to host config file as source or hosts in a comma separated string


        # create play with tasks
        play_source = dict(
            name="Ansible Play",
            hosts='all',
            gather_facts='no',
            tasks=[
                dict(action=dict(module='shell', args=cmd), register='shell_out')
            ]
        )
        play = Play().load(play_source, variable_manager=self.variable_manager, loader=self.loader)

        # actually run it
        tqm = None
        try:
            tqm = TaskQueueManager(
                inventory=self.inventory,
                variable_manager=self.variable_manager,
                loader=self.loader,
                options=self.options,
                passwords=self.passwords,
                stdout_callback=results_callback,  # Use our custom callback instead of the ``default`` callback plugin
            )
            result = tqm.run(play)
            return result
        finally:
            if tqm is not None:
                tqm.cleanup()
            os.remove(self.filename)
            # Remove ansible tmpdir
            shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)