from pygments import highlight
from pygments.formatters import BBCodeFormatter
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name

AVAILABLE_LANGS = ['Python', 'C', 'Cpp', 'Java', 'Rust', 'Javascript', 'Matlab']

def convert(source, _lex):
    lexer = get_lexer_by_name(_lex)
    data = highlight(source, lexer, BBCodeFormatter(
        codetag=True,
        style=get_style_by_name('default'),
        monofont=True
    ))
    return data
