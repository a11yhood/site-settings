---
title: Home
# metadata-files:
#   - _metadata.yml
layout: default
description: Accelerating the Adoption of open-Source Assistive Technology 
nav: false
permalink: index.html
---
> <dfn><strong>a11yhood</strong></dfn> Accelerating the Adoption of Open Source Assistive Technology

<figure>
<img title="a11yhood mockup" alt="A mockup of the a11yhood search functionality we are planning on adding. The website shows a search string titled 'draw smooth lines with a stylus on a digital tablet' and a series of results including a 3d printed wacom stylus grip with 5 stars, a mouse and tablet stabilizer available on github, a cushy pen grip from ravelry and a stroke stabilizer software from github. The user has selected the wacom stylus grip and it highlights skills needed and provides 3d printing instructions" src="images/allyhood.png"/>

<figcaption>The above image shows a mockup of the a11yhood search functionality we are planning on adding. The website shows a search string and a series of results including a 3d printed wacom stylus grip with 5 stars, a mouse and tablet stabilizer available on github, a cushy pen grip from ravelry and a stroke stabilizer software from github. Details of the stylus grip provide not only a link to the repository, but also a star rating and 3d printing instructions
</figcaption>
</figure>

## news

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
