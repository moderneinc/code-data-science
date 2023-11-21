__moderneColorMap = {
    'grey': {
        100: '#f8f9fa',
        150: '#edefef',
        200: '#e9ecef',
        300: '#dee2e6',
        400: '#ced4da',
        500: '#adb5bd',
        600: '#6c757d',
        700: '#495057',
        800: '#343a40',
        900: '#272C31'
    },
    'red': {
        'main': '#ff1947',
        100: '#ffe5eb',
        200: '#ffb2c2',
        300: '#ff7f99',
        400: '#ff4c70',
        500: '#e3163f',
        600: '#aa112f',
        700: '#710b20',
        800: '#390610'
    },
    'yellow': {
        'main': '#f9a91b',
        100: '#fef5e6',
        200: '#fde2b3',
        300: '#fccf80',
        400: '#fabc4e',
        500: '#dd9618',
        600: '#a67112',
        700: '#6f4b0c',
        800: '#372606'
    },
    'green': {
        'main': '#33ff99',
        100: '#e8fff4',
        200: '#bbffdd',
        300: '#8effc6',
        400: '#60ffb0',
        500: '#2de388',
        600: '#22aa66',
        700: '#177144',
        800: '#0b3922'
    },
    'blue': {
        'main': '#2e42ff',
        100: '#f6fafd',
        200: '#b9c0ff',
        300: '#8b96ff',
        400: '#5c6cff',
        500: '#293be3',
        600: '#1f2caa',
        700: '#141d71',
        800: '#0a0f39'
    },
    'indigo': {
        'main': '#00193c',
        50: '#f4f7fb',
        100: '#e3e5e9',
        200: '#aab2be',
        300: '#717f93',
        400: '#394c67',
        500: '#001635',
        600: '#001128',
        700: '#000b1b',
        800: '#00060d'
    },
    'black': {
        100: '#1e1e1e',
        800: '#121212'
    }
}

def colors_by_weight(weight):
    """
    Generate a list of moderne colors with the specified weight.
    Weights are 100, 200, 300, 400, 500, 600, 700, 800
    """
    return [
        __moderneColorMap['blue'][weight],
        __moderneColorMap['red'][weight],
        __moderneColorMap['yellow'][weight],
        __moderneColorMap['green'][weight],
        __moderneColorMap['indigo'][weight],
    ]
    
def color_gradient(color):
    """
    Generate a color weights for a specific color.
    Colors are 'blue', 'red', 'yellow', 'green', 'indigo'
    """
    return [
        __moderneColorMap[color][100],
        __moderneColorMap[color][200],
        __moderneColorMap[color][300],
        __moderneColorMap[color][400],
        __moderneColorMap[color][500],
        __moderneColorMap[color][600],
        __moderneColorMap[color][700],
        __moderneColorMap[color][800],
        
    ]

def generate_colors(int):
    """
    Generate a list of colors from the moderne color palette.
    Pass an option int to limit the number of colors returned.
    """
    colors = colors_by_weight("main") + colors_by_weight(300) + colors_by_weight(700) + colors_by_weight(500)
    if int is None:
        return colors 
    else:
        return colors[:int]


def qualitative(number: int = 0):
    if number == 500:
        return colors_by_weight(500)   
    else:
        return [
            __moderneColorMap['blue']['main'],
            __moderneColorMap['red']['main'],
            __moderneColorMap['yellow']['main'],
            __moderneColorMap['green']['main'],
            __moderneColorMap['indigo']['main'],
            '#db4197', # magenta
            '#7e9bd3', # periwinkle
            '#d6ffe2', # mint
        ]
