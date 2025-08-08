# Theme Update Instructions

Follow these steps to change the theme of the project:

1. Open the `input.css` file in your project.
2. Go to [https://tweakcn.com/editor/theme](https://tweakcn.com/editor/theme).
3. In the editor, select **Tailwind v4**.
4. Click on **Copy** to copy the generated CSS.
5. Paste the copied CSS into your `index.css` file, replacing the existing content. Keep these values on top:
    ```tailwind
    @layer theme, base, components, utilities;
    @import "tailwindcss/theme.css" layer(theme);
    @import "tailwindcss/preflight.css" layer(base);
    @import "tailwindcss/utilities.css" layer(utilities);
    ```

Run to update the index.css automatically.

```bash
./tailwind -i input.css -o static/index.css --watch
```

# Issues

1. Currently the border of the card and some input fields are white, even when there is an border set. Take a look at this [example](https://play.tailwindcss.com/BiIhHAQLXm?file=css). Maybe it comes because of TailwindCSS v4?


# Download TailwindCSS
| Because file is to large to place it in github.

```bash
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 && chmod +x tailwindcss-linux-x64 && mv tailwindcss-linux-x64 tailwind
```
