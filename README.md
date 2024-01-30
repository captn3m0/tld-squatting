---
layout: default
permalink: /
---

There's more than 1000 gTLDs delegated by ICANN. Unfortunately, a lot of owners of various TLDs have
decided to squat on them, and despite owning them for many years - these are not yet available
for registration.

Several of the brand gTLDs have been squatted by various corporations as well. The case
of Amazon.com, Inc. owning `.amazon` when several governments applied for it is well known.
But there are several smaller examples: `.apple` is owned by a technology company and apple
farmers can't use it (unlike `.kiwi` which can be used by Kiwi farmers.). Similarly `.mango` and `.orange` 
are also unavailable for registration, as are `.mint`, `.java`, `.ice`, `.food`, `.eat.

**Amazon** and **Google** own a bunch of such TLDs (40% of the below list) which are blocked from registrations
by the general public - `.book`, `.ads`, `.buy`, `.cal`, `.call`, `.circle`, `.docs`, `.drive`, `.eat`, 
`.fast`, `.fire`, `.free`, `.here`, and so on.

It is such a pity that corporations have decided to squat on these TLDs for several years
, and not allow them for registrations.

<table>
	<thead>
		<tr>
			<th>TLD</th>
			<!-- <th>Status</th> -->
			<th>Owner</th>
			<th>Type</th>
			<th>Domain Count</th>
		</tr>
	</thead>
	<tbody>

{% assign DATA = site.data.ntld|sort:'tld'%}
{% for T in DATA %}
{% assign count = site.data.domain_count[T.tld] |plus:0%}
{% if T.status!="GA" and site.data.fakebrands contains T.tld or site.rtypes contains T.type %}
<tr>
	<td>
		{{T.tld}}
		{% if site.data.punycode contains T.tld %}
		({{site.data.punycode[T.tld]}})
		{% endif %}
	</td>
	<!-- <td>{{T.status}}</td> -->
	<td>{{T.owner}}</td>
	<td>{{T.type}}</td>
	<td>{{count}}-{{count|times:10}}</td>
</tr>
{% endif %}
{% endfor %}
</tbody></table>


## Methodology

Source of the dataset is [nTLDStats](https://ntldstats.com/tld), with the following TLDs shown:

1. Curated list of BRAND TLDs (_data/fakebrands.yml). Contributions and corrections are welcome.
2. Unrestricted or Semi-restricted TLDs which are not in "GA".

Domain Counts for nTLDStats are known to be inaccurate, hence approximate ranges are shown instead.

## Why

Here's a list of some cool domains that you can't buy today (with what I'd do with some of them)

1. `bengaluru.cal` - A single events calendar for happenings in Bangalore
1. `block.analytics` - A petition to enforce DNT via regulation.
1. `block.ads` - redirects to uBO.
1. `software.bom` - Publish SBOMs.
1. `donot.call` - DNT submission
1. `bigger.data`
1. `linux.diy` - LFS + NAND2TETRIS speedrun.
1. `pleasemindthe.gap` - redirect to London metro.
1. `alphonso.mango` - 
1. `whatto.read` - fix my older [what-to-read project](https://github.com/captn3m0/what-to-read/), but use OpenLibrary and Bookwyrm instead.
1. `book.search` - ISBN OpenLibrary search.
1. `which.song` - Shazam alternative.
1. `blr.weather` - wttr.in/bengaluru
1. `much.wow` - RIP Doge
1. `fuck.you` - no explanation needed
1. `fuck.you.amazon` - please open registrations on `.zero`, `.you`, `.wow`, `.tushu`, `.tunes`, `.talk`, `.star`, `.smile`, `.spot`, .`silk`, `.secure`, `.save`, `.safe`, `.room`, `.read`, `.prime`, `.pin`, `.pay`, `.now`, `.like`, `.joy`, `.jot`, `.hot`, `.got`, `.free`, `.fire`, `.fast`, `.deal`, `.coupon`, `.circle`, `.call`, `.buy`, `.book`, `.author`, `.amazon`.
1. `fuck.you.google` - pleas open registrations on `.ads`, `.cal`, `.chrome`, `.docs`, `.drive`, `.eat`, `.hangout`, `.here`, `.map`, `.meet`, `.play`, `.search`.