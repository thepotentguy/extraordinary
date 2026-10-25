# R3.2.1 deployment record — 25 October 2026

The origin installer reports all five frozen R3.2.1 theme packages successfully uploaded and published. All 15 published stylesheet hashes, requested with fresh queries, match the approved ZIP members. The stored public-response hashes were independently checked against those members during this documentation update. Package hashes remain exactly those in `release-manifest.json`.

| Property | Published CSS matches | Native result/rate-view widths | Home evidence |
|---|---:|---|---|
| Kingfisher Villa Suites | 3/3 | 320, 390, 768, 1024, 1440, 1920px | Same six widths on R3.2; subsequent R3.2.1 change is scoped booking-button margins |
| Kwafubesi | 3/3 | Same six widths | R3.2.1, all six widths |
| Hoyo Hoyo | 3/3 | Same six widths | R3.2.1, all six widths |
| Hamiltons | 3/3 | Same six widths | R3.2.1, all six widths |
| Imbali | 3/3 | Same six widths | Same six widths on R3.2; subsequent R3.2.1 change is scoped booking-button margins |

The 30 recorded native result/rate-view checks and 30 recorded home checks show no horizontal document overflow and no temporary stylesheet override. They are bounded view checks, not proof of every state at every width. Installed Imbali1920 evidence shows the alternative-date button aligned with its parent and a 16px gap from the message. These observations supplement the preserved local fixture checks; they do not replace native input or full-journey acceptance.

## Outstanding qualifications

- **Ordinary visitor cache:** fresh-query verification proves the published files, not what every cached visitor currently receives. The ordinary stylesheet response had `max-age=14400` (four hours), and an older Imbali release was still observed there. Cached visitor rollout remains unverified.
- **Assets:** no logo or photograph was replaced. The cropper was blank and reported 0×0 in both browser routes, including an existing image editor. Editors were cancelled; no bypass or asset-update success is claimed.
- **Native issues:** Kwafubesi's property gallery remains empty at 1/0; mobile map issues remain unresolved. Do not describe that gallery as an image-loading pass. The previously missing mobileColor.css resource remains a separate legacy issue.
- **Acceptance scope:** no checkout or booking write occurred. Physical touch, comprehensive keyboard/screen-reader accessibility, complete checkout and business benefit remain uncertified. Published themes and view checks are delivery evidence, not sponsor acceptance.

This is a reviewed public summary of the origin's private final receipt. Raw browser evidence, publication screenshots and private operational records remain in the project lane and are not included in Git. This documentation update changed no implementation, theme package, CMS data or publication state.
