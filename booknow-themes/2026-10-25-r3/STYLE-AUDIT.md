# R3 shipped-style audit

All customer fixes are in source/corrections.css, compiled into both theme.css and mobileTheme.css in each archive. Later-screen inline CSS is restricted to review chrome and labelled placeholders.

| Treatment / selector | Source line | Destination |
|---|---:|---|
| `#content .hotelImage img` | 2 | `black-rhino2021/css/theme.css` and `mobileTheme.css` |
| `#content .ratesText p` | 3 | `black-rhino2021/css/theme.css` and `mobileTheme.css` |
| `#content button:disabled` | 4 | `black-rhino2021/css/theme.css` and `mobileTheme.css` |
| `.gwt-DialogBox:has(#gallery) #formButtons button` | 9 | `black-rhino2021/css/theme.css` and `mobileTheme.css` |
| `#content #formDetails` | 16 | `black-rhino2021/css/theme.css` and `mobileTheme.css` |
| `#newsFeeds .newsFeedFlexTable` | 104 | `black-rhino2021/css/theme.css` and `mobileTheme.css` |

Native hidden states and original gallery inline geometry are preserved. Local pages load extracted ZIP assets; 25 ZIP/source/HTTP hashes match. Clean Git fixture links use byte-identical source members. See verification-summary.json and per-property member manifests.
