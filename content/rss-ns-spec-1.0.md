---
title: "RR RSS Namespace Specification 1.0"
date: 2020-09-20T10:07:04+02:00
---
This namespace is an extension for the Reliability Report website following the [RSS 2.0 spec format](https://validator.w3.org/feed/docs/rss2.html).

## Changes

* _2020-09-20T10:37:12+02:00_ Initial version

## Namespace Declarations

`xmlns:rr="https://reliability.re/rss-ns-spec-1.0/"`

## Model

`<item>` Elements:

* `<rr:github>` Github's username of the item's curator (just the login name not the URL to the profile page).
* `<rr:twitter>` Twitter's username of the item's curator (just the login name not the URL to the profile page).
* `<rr:hashtags>` Hashtags that can be used to improve sharing on social media
* `<rr:plain>` A plain-text version of the item's curated content.

## Example

```xml
<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:rr="https://reliability.re/rss-ns-spec-1.0/">
  <channel>
    <title>Reliability Report</title>
    <link>https://reliability.re</link>
    <description>A site about Reliability Engineering</description>
    <language>en-us</language>
    <lastBuildDate>Fri, 18 Sep 2020 18:46:54 +0000</lastBuildDate>
    <item>
      <title>Debugging Go in prod using eBPF</title>
      <link>https://blog.pixielabs.ai/blog/</link>
      <pubDate>Fri, 18 Sep 2020 18:46:54 +0000</pubDate>
      <author>pabluk@users.noreply.github.com (pabluk)</author>
      <guid>2020-09-18-debugging-go-in-prod-using-ebpf</guid>
      <description>How to debug Go programs using &lt;b&gt;eBPF&lt;/b&gt;</description>
      <rr:github>pabluk</rr:github>
      <rr:twitter>pabluk</rr:twitter>
      <rr:hashtags>debugging,go,eBPF,linux</rr:hashtags>
      <rr:plain>How to debug Go programs using eBPF</rr:plain>
    </item>
  </channel>
</rss>
```
