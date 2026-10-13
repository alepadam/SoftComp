# =====================================================================
# Table helper (used by every Part 7 solution)
# =====================================================================
import pandas as pd
from IPython.display import display, HTML

def show_table(rows, columns, title=None, decimals=None):
    """Display a list of rows as a formatted table in the notebook.
    rows     : list of lists/tuples, one per table row
    columns  : list of column names (must be unique)
    title    : optional caption shown above the table
    decimals : fixed number of decimal places for floats
               (None = shortest form, e.g. 0.1 instead of 0.100000)"""
    df = pd.DataFrame(rows, columns=columns)

    def fmt(v):
        if isinstance(v, (float, np.floating)):
            return f"{v:.{decimals}f}" if decimals is not None else f"{v:g}"
        return v

    try:
        styler = df.style.hide(axis="index").format(fmt)
        styler = styler.set_properties(**{"text-align": "center"})
        styler = styler.set_table_styles([
            {"selector": "th", "props": [("text-align", "center"), ("padding", "4px 10px")]},
            {"selector": "td", "props": [("padding", "4px 10px")]},
            {"selector": "caption", "props": [("font-weight", "bold"), ("font-size", "1.05em"),
                                              ("text-align", "left"), ("padding-bottom", "6px")]},
        ])
        if title:
            styler = styler.set_caption(title)
        display(HTML(styler.to_html()))       # render now, so any error is caught below
    except Exception:
        # Fallback if pandas Styler is unavailable (e.g. jinja2 not installed)
        if title:
            print(title)
        display(df)