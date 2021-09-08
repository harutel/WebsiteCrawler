# Problem Statement

Write a web crawler using Python that crawls a single domain to scrape all of its internal URLs.

We want you to start by considering the following example domain, where the crawler should crawl the news pages and the comments, but not the links to articles on other domains:

https://news.ycombinator.com

However, the crawler should be capable of working on any domain.

The general rule is to crawl the first page, and all potential sub-pages but not any external URL's on other domains.

# Evaluation

Once execution is complete you should print the links (in any format) from each page on the domain to every other page on the same domain. E.g. if page A links to pages B and C you can print something like:
A -> B

A -> C

Suppose B had a further link to page D you'd also emit:

B -> D

The goal is to make the crawler work as efficiently as possible by using concurrent programming with the Python gevent library.