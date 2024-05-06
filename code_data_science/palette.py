__moderne_color_map = {
    "grey": {
        100: "#f8f9fa",
        150: "#edefef",
        200: "#e9ecef",
        300: "#dee2e6",
        400: "#ced4da",
        500: "#adb5bd",
        600: "#6c757d",
        700: "#495057",
        800: "#343a40",
        900: "#272C31",
    },
    "red": {
        "main": "#ff1947",
        100: "#ffe5eb",
        200: "#ffb2c2",
        300: "#ff7f99",
        400: "#ff4c70",
        500: "#e3163f",
        600: "#aa112f",
        700: "#710b20",
        800: "#390610",
    },
    "yellow": {
        "main": "#f9a91b",
        100: "#fef5e6",
        200: "#fde2b3",
        300: "#fccf80",
        400: "#fabc4e",
        500: "#dd9618",
        600: "#a67112",
        700: "#6f4b0c",
        800: "#372606",
    },
    "green": {
        "main": "#33ff99",
        100: "#e8fff4",
        200: "#bbffdd",
        300: "#8effc6",
        400: "#60ffb0",
        500: "#2de388",
        600: "#22aa66",
        700: "#177144",
        800: "#0b3922",
    },
    "blue": {
        "main": "#2e42ff",
        100: "#f6fafd",
        200: "#b9c0ff",
        300: "#8b96ff",
        400: "#5c6cff",
        500: "#293be3",
        600: "#1f2caa",
        700: "#141d71",
        800: "#0a0f39",
    },
    "indigo": {
        "main": "#00193c",
        50: "#f4f7fb",
        100: "#e3e5e9",
        200: "#aab2be",
        300: "#717f93",
        400: "#394c67",
        500: "#001635",
        600: "#001128",
        700: "#000b1b",
        800: "#00060d",
    },
    "black": {100: "#1e1e1e", 800: "#121212"},
    # Cool palette
    "midnight": {
        100: "#CCD1D8",
        300: "#66768B",
        500: "#001A3E",
        700: "#001025",
    },
    "periwinkle": {
        100: "#E5EBF6",
        300: "#B2C3E4",
        500: "#7E9BD3",
        700: "#4C5D7E",
    },
    "digital_blue": {
        100: "#D5D9FF",
        300: "#828EFF",
        500: "#2F42FF",
        700: "#1C2899",
    },
    "sage": {
        100: "#F3FAF4",
        300: "#DCEFDE",
        500: "#C4E5C8",
        700: "#768978",
    },
    "activity_green": {
        100: "#D4EEE7",
        300: "#7DCCB8",
        500: "#27AA88",
        700: "#176652",
    },
    # Warm palette
    "amber": {
        100: "#FBEED4",
        300: "#FBCB76",
        500: "#F9A91B",
        700: "#956510",
    },
    "golden": {
        100: "#FAF2D6",
        300: "#FEE968",
        500: "#FDDA04",
        700: "#8E6E13",
    },
    "sunshine": {
        100: "#FEF9D2",
        300: "#FAEA7C",
        500: "#F8DC4A",
        700: "#958329",
    },
    "cherry_red": {
        100: "#FFD3D3",
        300: "#FF8484",
        500: "#FF3232",
        700: "#991E1E",
    },
    "magenta": {
        100: "#F3DAE9",
        300: "#DD92BF",
        500: "#DB4197",
        700: "#83275B",
    },
    "lavender": {
        100: "#EBD5F1",
        300: "#C282D5",
        500: "#992FB9",
        700: "#5C1C6F",
    },
}

_moderne_brand_scale = [
    __moderne_color_map["digital_blue"][500],
    __moderne_color_map["periwinkle"][500],
    __moderne_color_map["activity_green"][500],
    __moderne_color_map["sage"][300],
    __moderne_color_map["activity_green"][300],
    __moderne_color_map["amber"][500],
    __moderne_color_map["magenta"][500],
    __moderne_color_map["lavender"][500],
    __moderne_color_map["digital_blue"][100],
    __moderne_color_map["cherry_red"][500],
]


def colors_by_weight(weight):
    """
    Generate a list of moderne colors with the specified weight.
    Weights are 100, 300, 500, 700
    """
    return [
        __moderne_color_map["digital_blue"][weight],
        __moderne_color_map["midnight"][weight],
        __moderne_color_map["activity_green"][weight],
        __moderne_color_map["sage"][weight],
        __moderne_color_map["periwinkle"][weight],
    ]


def color_gradient(color):
    """
    Generate a color weights for a specific color.
    Colors are 'blue', 'red', 'yellow', 'green', 'indigo'
    """
    return [
        __moderne_color_map[color][100],
        __moderne_color_map[color][200],
        __moderne_color_map[color][300],
        __moderne_color_map[color][400],
        __moderne_color_map[color][500],
        __moderne_color_map[color][600],
        __moderne_color_map[color][700],
        __moderne_color_map[color][800],
    ]


def generate_colors(integer):
    """
    Generate a list of colors from the moderne color palette.
    Pass an option int to limit the number of colors returned.
    """
    colors = (
        colors_by_weight(500)
        + colors_by_weight(300)
        + colors_by_weight(700)
        + colors_by_weight(100)
    )
    if integer is None:
        return colors
    else:
        return colors[:integer]


def qualitative():
    """
    Generate a list of colors for qualitative data.
    """

    return _moderne_brand_scale
