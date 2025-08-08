from fasthtml.common import *


hdrs = Link(href="/static/index.css", rel="stylesheet")

app = FastHTML(
    hdrs=hdrs,
    cls="bg-background text-foreground p-6",
    default_hdrs=False,
    htmlkw={"class": "dark"},
)
app.mount("/static", StaticFiles(directory="static"), name="static")


def theme_toggle():
    return Button(
        "Toggle Theme",
        onclick="document.documentElement.classList.toggle('dark');",
        cls="inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 bg-primary text-primary-foreground shadow hover:bg-primary/90 h-8 rounded-md px-3 text-xs mb-4",
    )


# TODO
# https://play.tailwindcss.com/BiIhHAQLXm?file=css shows a normal border....


def ShadTest(enabled=False):
    if not enabled:
        return
    from components.ui.button import Button as ShadButton
    from components.ui.card import (
        Card as ShadCard,
        CardHeader as ShadCardHeader,
        CardTitle as ShadCardTitle,
        CardDescription as ShadCardDescription,
        CardContent as ShadCardContent,
        CardFooter as ShadCardFooter,
    )

    return (
        ShadCard(
            ShadCardHeader(
                ShadCardTitle("Create a post"),
                ShadCardDescription("Enter your post title below."),
            ),
            ShadCardContent(
                ShadButton("Default Button", variant="default"),
                ShadButton("Destructive Button", variant="destructive"),
                ShadButton("Outline Button", variant="outline"),
                ShadButton("Secondary Button", variant="secondary"),
                ShadButton("Ghost Button", variant="ghost"),
                ShadButton("Link Button", variant="link"),
                cls="flex flex-col space-y-4",
            ),
            ShadCardFooter(
                Div(
                    ShadButton("Cancel", variant="outline"),
                    ShadButton("Submit"),
                    cls="flex w-full justify-end gap-2",
                ),
            ),
            standard=True,
            cls="mb-4",
        ),
    )


@app.get("/")
def home():
    return (
        theme_toggle(),
        ShadTest(enabled=True),
        Div(
            Div(
                Div(
                    Div(
                        "Upgrade your subscription",
                        cls="font-semibold tracking-tight text-lg",
                    ),
                    Div(
                        "You are currently on the free plan. Upgrade to the pro plan to get access to all features.",
                        cls="text-sm text-muted-foreground text-balance",
                    ),
                    cls="flex flex-col space-y-1.5 p-6",
                ),
                Div(
                    Div(
                        Div(
                            Div(
                                Label(
                                    "Name",
                                    fr="name",
                                    cls="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
                                ),
                                Input(
                                    id="name",
                                    placeholder="Evil Rabbit",
                                    cls="flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
                                ),
                                cls="flex flex-1 flex-col gap-2",
                            ),
                            Div(
                                Label(
                                    "Email",
                                    fr="email",
                                    cls="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
                                ),
                                Input(
                                    id="email",
                                    placeholder="example@acme.com",
                                    cls="flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
                                ),
                                cls="flex flex-1 flex-col gap-2",
                            ),
                            cls="flex flex-col gap-3 @3xl:flex-row",
                        ),
                        Div(
                            Label(
                                "Card Number",
                                fr="card-number",
                                cls="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
                            ),
                            Div(
                                Input(
                                    id="card-number",
                                    placeholder="1234 1234 1234 1234",
                                    cls="flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm col-span-2 @3xl:col-span-1",
                                ),
                                Input(
                                    id="card-number-expiry",
                                    placeholder="MM/YY",
                                    cls="flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
                                ),
                                Input(
                                    id="card-number-cvc",
                                    placeholder="CVC",
                                    cls="flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
                                ),
                                cls="grid grid-cols-2 gap-3 @3xl:grid-cols-[1fr_80px_60px]",
                            ),
                            cls="flex flex-col gap-2",
                        ),
                        Fieldset(
                            Legend("Plan", cls="text-sm font-medium"),
                            P(
                                "Select the plan that best fits your needs.",
                                cls="text-muted-foreground text-sm",
                            ),
                            Div(
                                Label(
                                    Button(
                                        Span(
                                            data_state="checked",
                                            cls="flex items-center justify-center",
                                        ),
                                        type="button",
                                        role="radio",
                                        aria_checked="true",
                                        data_state="checked",
                                        value="starter",
                                        id="Starter Plan",
                                        tabindex="-1",
                                        data_radix_collection_item="",
                                        cls="aspect-square h-4 w-4 rounded-full border border-primary text-primary ring-offset-background focus:outline-hidden focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:border-primary",
                                    ),
                                    Div(
                                        Div("Starter Plan", cls="font-medium"),
                                        Div(
                                            "Perfect for small businesses.",
                                            cls="text-muted-foreground text-xs leading-snug text-balance",
                                        ),
                                        cls="grid gap-1 font-normal",
                                    ),
                                    cls="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 has-[[data-state=checked]]:border-ring has-[[data-state=checked]]:bg-input/20 flex items-start gap-3 rounded-lg border p-3",
                                ),
                                Label(
                                    Button(
                                        type="button",
                                        role="radio",
                                        aria_checked="false",
                                        data_state="unchecked",
                                        value="pro",
                                        id="Pro Plan",
                                        tabindex="-1",
                                        data_radix_collection_item="",
                                        cls="aspect-square h-4 w-4 rounded-full border border-primary text-primary ring-offset-background focus:outline-hidden focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:border-primary",
                                    ),
                                    Div(
                                        Div("Pro Plan", cls="font-medium"),
                                        Div(
                                            "More features and storage.",
                                            cls="text-muted-foreground text-xs leading-snug text-balance",
                                        ),
                                        cls="grid gap-1 font-normal",
                                    ),
                                    cls="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 has-[[data-state=checked]]:border-ring has-[[data-state=checked]]:bg-input/20 flex items-start gap-3 rounded-lg border p-3",
                                ),
                                role="radiogroup",
                                aria_required="false",
                                dir="ltr",
                                tabindex="0",
                                style="outline: none;",
                                cls="grid gap-3 @3xl:grid-cols-2",
                            ),
                            cls="flex flex-col gap-3",
                        ),
                        Div(
                            Label(
                                "Notes",
                                fr="notes",
                                cls="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
                            ),
                            Textarea(
                                id="notes",
                                placeholder="Enter notes",
                                cls="flex min-h-[60px] w-full rounded-md border border-input bg-transparent px-3 py-2 text-base shadow-sm placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
                            ),
                            cls="flex flex-col gap-2",
                        ),
                        Div(
                            Div(
                                Button(
                                    type="button",
                                    role="checkbox",
                                    aria_checked="false",
                                    data_state="unchecked",
                                    value="on",
                                    id="terms",
                                    cls="peer h-4 w-4 shrink-0 rounded-sm border border-primary ring-offset-background focus-visible:outline-hidden focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground",
                                ),
                                Label(
                                    "I agree to the terms and conditions",
                                    fr="terms",
                                    cls="text-sm leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 font-normal",
                                ),
                                cls="flex items-center gap-2",
                            ),
                            Div(
                                Button(
                                    Span(
                                        data_state="checked",
                                        style="pointer-events: none;",
                                        cls="flex items-center justify-center text-current",
                                    ),
                                    type="button",
                                    role="checkbox",
                                    aria_checked="true",
                                    data_state="checked",
                                    value="on",
                                    id="newsletter",
                                    cls="peer h-4 w-4 shrink-0 rounded-sm border border-primary ring-offset-background focus-visible:outline-hidden focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground",
                                ),
                                Label(
                                    "Allow us to send you emails",
                                    fr="newsletter",
                                    cls="text-sm leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 font-normal",
                                ),
                                cls="flex items-center gap-2",
                            ),
                            cls="flex flex-col gap-3",
                        ),
                        cls="flex flex-col gap-6",
                    ),
                    cls="p-6 pt-0",
                ),
                Div(
                    Button(
                        "Cancel",
                        cls="inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground h-8 rounded-md px-3 text-xs",
                    ),
                    Button(
                        "Upgrade Plan",
                        cls="inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 bg-primary text-primary-foreground shadow hover:bg-primary/90 h-8 rounded-md px-3 text-xs",
                    ),
                    cls="items-center p-6 pt-0 flex justify-between",
                ),
                cls="rounded-xl border bg-card text-card-foreground shadow",
            ),
            Div(
                Div(
                    Div(
                        "Team Members", cls="font-semibold leading-none tracking-tight"
                    ),
                    Div(
                        "Invite your team members to collaborate.",
                        cls="text-sm text-muted-foreground",
                    ),
                    cls="flex flex-col space-y-1.5 p-6",
                ),
                Div(
                    Div(
                        Div(
                            Span(
                                Span(
                                    "S",
                                    cls="flex h-full w-full items-center justify-center rounded-full bg-muted",
                                ),
                                cls="relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full border",
                            ),
                            Div(
                                P(
                                    "Sofia Davis",
                                    cls="text-sm leading-none font-medium",
                                ),
                                P("m@example.com", cls="text-muted-foreground text-xs"),
                                cls="flex flex-col gap-0.5",
                            ),
                            cls="flex items-center gap-4",
                        ),
                        Button(
                            "Owner",
                            type="button",
                            aria_haspopup="dialog",
                            aria_expanded="false",
                            aria_controls="radix-_r_10c_",
                            data_state="closed",
                            cls="inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-8 rounded-md px-3 text-xs ml-auto shadow-none",
                        ),
                        cls="flex items-center justify-between gap-4",
                    ),
                    Div(
                        Div(
                            Span(
                                Span(
                                    "J",
                                    cls="flex h-full w-full items-center justify-center rounded-full bg-muted",
                                ),
                                cls="relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full border",
                            ),
                            Div(
                                P(
                                    "Jackson Lee",
                                    cls="text-sm leading-none font-medium",
                                ),
                                P("p@example.com", cls="text-muted-foreground text-xs"),
                                cls="flex flex-col gap-0.5",
                            ),
                            cls="flex items-center gap-4",
                        ),
                        Button(
                            "Developer",
                            type="button",
                            aria_haspopup="dialog",
                            aria_expanded="false",
                            aria_controls="radix-_r_10d_",
                            data_state="closed",
                            cls="inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-8 rounded-md px-3 text-xs ml-auto shadow-none",
                        ),
                        cls="flex items-center justify-between gap-4",
                    ),
                    Div(
                        Div(
                            Span(
                                Span(
                                    "I",
                                    cls="flex h-full w-full items-center justify-center rounded-full bg-muted",
                                ),
                                cls="relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full border",
                            ),
                            Div(
                                P(
                                    "Isabella Nguyen",
                                    cls="text-sm leading-none font-medium",
                                ),
                                P("i@example.com", cls="text-muted-foreground text-xs"),
                                cls="flex flex-col gap-0.5",
                            ),
                            cls="flex items-center gap-4",
                        ),
                        Button(
                            "Billing",
                            type="button",
                            aria_haspopup="dialog",
                            aria_expanded="false",
                            aria_controls="radix-_r_10e_",
                            data_state="closed",
                            cls="inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-8 rounded-md px-3 text-xs ml-auto shadow-none",
                        ),
                        cls="flex items-center justify-between gap-4",
                    ),
                    cls="p-6 pt-0 grid gap-6",
                ),
                cls="rounded-xl border bg-card text-card-foreground shadow",
            ),
            Div(
                Div(
                    Div(
                        "Cookie Settings",
                        cls="font-semibold leading-none tracking-tight",
                    ),
                    Div(
                        "Manage your cookie settings here.",
                        cls="text-sm text-muted-foreground",
                    ),
                    cls="flex flex-col space-y-1.5 p-6",
                ),
                Div(
                    Div(
                        Label(
                            Span("Strictly Necessary"),
                            Span(
                                "These cookies are essential in order to use the website and use its features.",
                                cls="text-muted-foreground leading-snug font-normal",
                            ),
                            fr="necessary",
                            cls="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 flex flex-col items-start",
                        ),
                        Button(
                            Span(
                                data_state="checked",
                                cls="pointer-events-none block h-5 w-5 rounded-full bg-background shadow-lg ring-0 transition-transform data-[state=checked]:translate-x-5 data-[state=unchecked]:translate-x-0",
                            ),
                            type="button",
                            role="switch",
                            aria_checked="true",
                            data_state="checked",
                            value="on",
                            id="necessary",
                            aria_label="Necessary",
                            cls="peer inline-flex h-6 w-11 shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent transition-colors focus-visible:outline-hidden focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=unchecked]:bg-input",
                        ),
                        cls="flex items-center justify-between gap-4",
                    ),
                    Div(
                        Label(
                            Span("Functional Cookies"),
                            Span(
                                "These cookies allow the website to provide personalized functionality.",
                                cls="text-muted-foreground leading-snug font-normal",
                            ),
                            fr="functional",
                            cls="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 flex flex-col items-start",
                        ),
                        Button(
                            Span(
                                data_state="unchecked",
                                cls="pointer-events-none block h-5 w-5 rounded-full bg-background shadow-lg ring-0 transition-transform data-[state=checked]:translate-x-5 data-[state=unchecked]:translate-x-0",
                            ),
                            type="button",
                            role="switch",
                            aria_checked="false",
                            data_state="unchecked",
                            value="on",
                            id="functional",
                            aria_label="Functional",
                            cls="peer inline-flex h-6 w-11 shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent transition-colors focus-visible:outline-hidden focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=unchecked]:bg-input",
                        ),
                        cls="flex items-center justify-between gap-4",
                    ),
                    cls="p-6 pt-0 grid gap-6",
                ),
                Div(
                    Button(
                        "Save preferences",
                        cls="inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2 w-full",
                    ),
                    cls="flex items-center p-6 pt-0",
                ),
                cls="rounded-xl border bg-card text-card-foreground shadow",
            ),
            Div(
                Div(
                    Div(
                        Div(
                            Div(
                                Div(
                                    "tweakcn",
                                    cls="font-semibold leading-none tracking-tight",
                                ),
                                Div(
                                    "A visual editor for shadcn/ui components with beautiful themes. Accessible. Customizable. Open Source.",
                                    cls="text-sm text-muted-foreground",
                                ),
                                cls="space-y-1.5",
                            ),
                            Div(
                                A(
                                    Button(
                                        "Star",
                                        cls="justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 bg-secondary text-secondary-foreground hover:bg-secondary/80 h-9 py-2 flex items-center gap-2 px-3 shadow-none",
                                    ),
                                    href="https://github.com/jnsahaj/tweakcn",
                                ),
                                cls="bg-secondary text-secondary-foreground flex min-w-20 shrink-0 items-center space-x-1 rounded-md",
                            ),
                            cls="flex items-start justify-between gap-4",
                        ),
                        cls="flex flex-col space-y-1.5 p-6",
                    ),
                    Div(
                        Div(
                            Div("TypeScript", cls="flex items-center"),
                            Div("20k", cls="flex items-center"),
                            Div("Updated April 2023"),
                            cls="text-muted-foreground flex space-x-4 text-sm",
                        ),
                        cls="p-6 pt-0",
                    ),
                    cls="rounded-xl border bg-card text-card-foreground shadow",
                ),
                Div(
                    Div(
                        Div(
                            "Date picker with range",
                            cls="font-semibold leading-none tracking-tight",
                        ),
                        Div(
                            "Select a date range.", cls="text-sm text-muted-foreground"
                        ),
                        cls="flex flex-col space-y-1.5 p-6",
                    ),
                    Div(
                        Button(
                            "Jan 20, 2022 - Feb 09, 2022",
                            id="date",
                            type="button",
                            aria_haspopup="dialog",
                            aria_expanded="false",
                            aria_controls="radix-_r_10f_",
                            data_state="closed",
                            cls="inline-flex items-center gap-2 whitespace-nowrap rounded-md text-sm transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2 w-full max-w-[300px] justify-start text-left font-normal",
                        ),
                        cls="p-6 pt-0",
                    ),
                    cls="rounded-xl border bg-card text-card-foreground shadow grid gap-2",
                ),
                cls="hidden flex-col gap-4 @7xl:flex",
            ),
            cls="flex flex-col gap-4",
        ),
    )


serve()
