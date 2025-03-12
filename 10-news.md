---
title: News
layout: default
permalink: news.html
---
# News

<ul>
  {% for post in site.posts %}
    <li>
    <p>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span>{{ post.description }}</span>
    </p>
    </li>
  {% endfor %}
</ul>
