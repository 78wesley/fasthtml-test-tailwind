from fasthtml.common import *


hdrs = (
    Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"),
    StyleX("index.css", type="text/tailwindcss"),
)

app = FastHTML(
    hdrs=hdrs,
    htmlkw={
        "class": "dark",
    },
    cls="bg-background",
    style="",
)


def theme_toggle():
    return Button(
        "Toggle Theme",
        cls="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive bg-primary text-primary-foreground shadow-xs hover:bg-primary/90 h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
        onclick="document.documentElement.classList.toggle('dark');",
    )


# TODO for some reason the borders are white...


@app.route("/")
def index():
    # create an example forum that shows input button selection dropdown and theme toggle
    return theme_toggle(), Main(
        H1(
            "Tailwind CSS Test Page",
            cls="text-4xl font-bold text-blue-600 mb-8 flex items-center gap-2",
        ),
        Div(
            Div(
                Div(
                    H2("Card 1", cls="text-2xl font-semibold text-gray-800"),
                    cls="flex items-center gap-2 mb-4",
                ),
                P("This is a test card with Tailwind CSS styling.", cls="text-gray-600"),
                cls="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow",
            ),
            Div(
                Div(
                    H2("Card 2", cls="text-2xl font-semibold text-gray-800"),
                    cls="flex items-center gap-2 mb-4",
                ),
                P("Another test card with different styling.", cls="text-gray-600"),
                cls="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow",
            ),
            Div(
                Div(
                    H2("Card 3", cls="text-2xl font-semibold text-gray-800"),
                    cls="flex items-center gap-2 mb-4",
                ),
                P("A third card to test grid layout.", cls="text-gray-600"),
                cls="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow",
            ),
            cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8",
        ),
        Div(
            Div(
                Button(
                    "Primary Button",
                    cls="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 border-none bg-primary text-primary-foreground shadow hover:bg-primary/90 h-9 px-4 py-2",
                ),
                Button(
                    "Secondary Button",
                    cls="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-secondary text-secondary-foreground shadow-sm border-solid border border-border hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2",
                ),
                Button(
                    "Destructive Button",
                    cls="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-secondary text-destructive border-solid border border-destructive shadow-sm hover:bg-destructive/10 h-9 px-4 py-2",
                ),
                cls="flex gap-4",
            ),
            Div(
                Button(
                    "Outline Button",
                    cls="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-secondary text-secondary-foreground shadow-sm border-solid border border-border hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2",
                ),
                Button(
                    "Ghost Button",
                    cls="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 border-none bg-transparent hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2",
                ),
                Button(
                    "Link Button",
                    cls="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 border-none bg-transparent text-primary underline-offset-4 hover:underline h-9 px-4 py-2",
                ),
                cls="flex gap-4",
            ),
            cls="space-y-4 mb-8",
        ),
        Div(
            Div(
                Label(
                    "Username",
                    fr="username",
                    cls="text-gray-700 text-sm font-bold mb-2 flex items-center gap-2",
                ),
                Div(
                    Input(
                        id="username",
                        placeholder="Username",
                        cls="shadow appearance-none border rounded w-full py-2 pl-10 pr-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                    ),
                    cls="relative",
                ),
                cls="mb-4",
            ),
            Div(
                Label(
                    "Password",
                    fr="password",
                    cls="text-gray-700 text-sm font-bold mb-2 flex items-center gap-2",
                ),
                Div(
                    Input(
                        id="password",
                        type="password",
                        placeholder="******************",
                        cls="shadow appearance-none border rounded w-full py-2 pl-10 pr-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline",
                    ),
                    cls="relative",
                ),
                cls="mb-6",
            ),
            cls="max-w-md",
        ),
        Div(
            Div(
                Div(P("Warning!", cls="font-bold"), P("This is a test alert message using Tailwind CSS.")),
                role="alert",
                cls="bg-yellow-100 border-l-4 border-yellow-500 text-yellow-700 p-4 flex items-start gap-2",
            ),
            Div(
                Div(P("Success!", cls="font-bold"), P("This is a success message with an icon.")),
                role="alert",
                cls="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 flex items-start gap-2",
            ),
            Div(
                Div(P("Info", cls="font-bold"), P("This is an informational message with an icon.")),
                role="alert",
                cls="bg-blue-100 border-l-4 border-blue-500 text-blue-700 p-4 flex items-start gap-2",
            ),
            cls="space-y-4",
        ),
        cls="container mx-auto px-4 py-8",
    )


serve()
