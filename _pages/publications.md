---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

For more detailed and comprehensive information on all of my publications, please refer to my **[Google Scholar account](https://scholar.google.com/citations?user=VtFoSwsAAAAJ&hl=en)**.

**<center> Citation Graph per Year from Google Scholar </center>**

<center>
<iframe width="302" height="186" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSKmjxmBs_pogXpYW0tRjDJQMFdT2CueX9xRBaWt8LgjfUcRlponSrbPemVOb4RbBbfBavdtt0Kw0PX/pubchart?oid=843272523&amp;format=interactive"></iframe>
</center>


Below, you can find summaries, related information for each publication, and download the respective papers.

## Hamid's Publication Archie

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
