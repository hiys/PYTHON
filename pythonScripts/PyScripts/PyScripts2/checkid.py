import string
import keyword

first_chs = string.ascii_letters + '_'
all_chs = first_chs + string.digits

def check_id(idt):   # abc@123
    if idt[0] not in first_chs:
        return '第一个字符不合法'

    for ind, ch in enumerate(idt[1:]):  # bc@123 [(0, b), (1, c)...]
        if ch not in all_chs:
            return '第%s个字符%s非法' % (ind+2, ch)

    if keyword.iskeyword(idt):
        return '%s是关键字，不能作为自定义的标识符' % idt

    return '%s是合法的标识符' % idt


if __name__ == '__main__':
    idt = input('请输入待检查的标识符：')
    print(check_id(idt))
