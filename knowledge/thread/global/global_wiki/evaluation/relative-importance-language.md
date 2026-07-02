---
auto_generated: true
entity_type: concept
id: global-relative-importance-language
last_updated: 2026-06-18
name: "Relative Importance Language"
source_module: evaluation
title: "Relative Importance Language"
trust: trusted
type: concept
updated: "'2026-04-22T23:01:17'"
---

> **Entity type:** `concept`

Section M language signals factor weighting even when numerical weights are not stated. Decoder: 'significantly more important than' = ~2x weight; 'more important than' = ~1.3-1.5x weight; 'approximately equal to' = same weight; 'when combined, non-price factors are significantly more important than price' = best-value tradeoff with strong technical preference; 'when combined, approximately equal to price' = price will likely decide between technically close offers; 'price is the least important factor' does NOT mean price is unimportant — it means technical differentiation must be substantial to overcome price delta. Misreading these phrases is a top capture-strategy error.

## Related
- [[capture-llm-wiki]]
- [[price-to-win-analysis]]
- [[firm-fixed-pricing]]
- [[ffp-shaping-radar]]
- [[non-fixed-pricing]]
- [[pricing-buckets]]
- [[best-value-tradeoff-analysis]]
