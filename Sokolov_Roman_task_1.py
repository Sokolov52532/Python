import re

RE_MAIL = re.compile(r'(\w+)@(?<=@)(\w+\.{1}[a-z]{2,4}\Z)')
email = input(r"Введите e-mail: ")


def mail_parser(mail):
    result = {k: v for i in RE_MAIL.findall(mail) for k, v in zip(('username', 'domain'), i)}

    if len(RE_MAIL.findall(mail)) == 0:
        raise ValueError(f'wrong email: {mail}')

    return result


print(mail_parser(email))
