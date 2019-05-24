import requests

s = requests.Session()
reponse = s.post("http://www.jeasyui.com/demo/main/datagrid2_getdata.php",
                 data={'page':1,'rows':30})
print(reponse.json())