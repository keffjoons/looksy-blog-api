from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import Optional

# Initialize FastAPI app
app = FastAPI(
    title="Framer CMS Content API",
    description="REST API for programmatic SEO blog publishing to Framer",
    version="1.0.0"
)

# CORS middleware for Framer access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for blog posts
POSTS_DATA = {
    "virtual-try-on-luxury-fashion-roi-guide": {
        "id": "post-1",
        "slug": "virtual-try-on-luxury-fashion-roi-guide",
        "title": "Virtual Try-On for Luxury Fashion: ROI Analysis & Implementation Guide",
        "excerpt": "How luxury fashion brands are achieving 40% higher conversion rates and 25% reduced returns with AI-powered virtual try-on technology.",
        "content": """<h1>Virtual Try-On for Luxury Fashion: ROI Analysis & Implementation Guide</h1><p>The luxury fashion industry faces a unique challenge: customers want to experience the quality, fit, and feel of premium products before committing to a purchase. Virtual try-on technology bridges this gap, delivering measurable ROI for premium brands.</p><h2>The ROI Case for Luxury Virtual Try-On</h2><p>Our enterprise clients in luxury fashion consistently report:</p><ul><li><strong>40% higher conversion rates</strong> on product pages with virtual try-on</li><li><strong>25% reduction in return rates</strong>, critical for high-value items</li><li><strong>3x longer session duration</strong> as customers engage with the technology</li><li><strong>15% increase in average order value</strong> through confident purchasing</li></ul><h2>Implementation Roadmap</h2><p>For luxury brands, implementation requires attention to detail that matches your brand standards:</p><h3>Phase 1: Foundation (Weeks 1-2)</h3><ul><li>Product photography integration</li><li>Style guide alignment</li><li>Initial model training on your product catalog</li></ul><h3>Phase 2: Integration (Weeks 3-4)</h3><ul><li>Website widget deployment</li><li>Mobile optimization</li><li>Analytics configuration</li></ul><h3>Phase 3: Optimization (Ongoing)</h3><ul><li>A/B testing variants</li><li>Conversion rate optimization</li><li>Expansion to full catalog</li></ul>""",
        "author": "Looksy Team",
        "tags": ["luxury-fashion", "roi", "implementation", "enterprise"],
        "meta_title": "Virtual Try-On for Luxury Fashion: ROI Analysis & Implementation Guide",
        "meta_description": "How luxury fashion brands achieve 40% higher conversion rates and 25% reduced returns with AI-powered virtual try-on technology.",
        "published_at": "2026-02-09T10:00:00Z",
        "status": "published"
    },
    "beauty-brand-virtual-try-on-conversion": {
        "id": "post-2",
        "slug": "beauty-brand-virtual-try-on-conversion",
        "title": "Beauty Brand Virtual Try-On: Increasing Conversion by 30% with AI",
        "excerpt": "Beauty brands using virtual try-on see 30% conversion increases. Learn implementation strategies for makeup, skincare, and hair color brands.",
        "content": """<h1>Beauty Brand Virtual Try-On: Increasing Conversion by 30% with AI</h1><p>The beauty industry has been revolutionized by virtual try-on technology. From lipsticks to foundations, customers now expect to see products on their own faces before purchasing.</p><h2>Why Beauty Brands Need Virtual Try-On</h2><p>The numbers tell a compelling story:</p><ul><li><strong>30% conversion rate increase</strong> on product pages with try-on functionality</li><li><strong>50% reduction in product returns</strong> for color cosmetics</li><li><strong>2.5x engagement time</strong> when customers use virtual try-on</li><li><strong>35% of customers</strong> say virtual try-on increases purchase confidence</li></ul><h2>Category-Specific Strategies</h2><h3>Makeup & Color Cosmetics</h3><p>Foundation matching and lipstick try-on are the highest-ROI implementations. Focus on:</p><ul><li>Accurate skin tone matching across diverse complexions</li><li>Realistic texture rendering (matte, gloss, metallic)</li><li>Multi-product looks (complete makeup application)</li></ul><h3>Skincare</h3><p>While you cannot try on skincare, virtual technology helps with:</p><ul><li>Skin concern visualization (before/after simulation)</li><li>Product texture and application demonstrations</li><li>Personalized routine recommendations</li></ul><h3>Hair Color</h3><p>Hair color try-on has the highest engagement rates:</p><ul><li>Real-time color preview on customer's own photo</li><li>Multiple shade comparisons side-by-side</li><li>Growth root visualization for maintenance planning</li></ul>""",
        "author": "Looksy Team",
        "tags": ["beauty", "conversion", "makeup", "skincare"],
        "meta_title": "Beauty Brand Virtual Try-On: 30% Conversion Increase with AI",
        "meta_description": "Beauty brands using virtual try-on see 30% conversion increases. Learn implementation strategies for makeup, skincare, and hair color brands.",
        "published_at": "2026-02-09T10:30:00Z",
        "status": "published"
    },
    "virtual-try-on-enterprise-tech-stack": {
        "id": "post-3",
        "slug": "virtual-try-on-enterprise-tech-stack",
        "title": "Enterprise Guide: Integrating Virtual Try-On with Your Tech Stack",
        "excerpt": "Technical guide for CTOs and engineering teams: integrating virtual try-on with Shopify, Magento, Salesforce Commerce Cloud, and custom platforms.",
        "content": """
<h1>Enterprise Guide: Integrating Virtual Try-On with Your Tech Stack</h1>
<p>For enterprise retailers, virtual try-on integration isn't just about the frontend experience. It requires seamless integration with your existing commerce infrastructure, from product information management to order processing.</p>
<h2>Platform-Specific Integration Guides</h2>
<h3>Shopify & Shopify Plus</h3>
<p>The most straightforward integration path for mid-market brands:</p>
<ul>
<li><strong>App Store Installation:</strong> Direct install from Shopify App Store</li>
<li><strong>Theme Integration:</strong> Single code snippet in product.liquid</li>
<li><strong>Product Sync:</strong> Automatic catalog synchronization</li>
<li><strong>Timeline:</strong> 1-2 days to production</li>
</ul>
<h3>Magento (Adobe Commerce)</h3>
<p>Enterprise-grade flexibility with custom integration options:</p>
<ul>
<li><strong>Extension Installation:</strong> Composer package for Magento 2</li>
<li><strong>Custom Theming:</strong> Full control over widget appearance</li>
<li><strong>API Integration:</strong> Direct REST API access for custom builds</li>
<li><strong>Timeline:</strong> 1-2 weeks for custom implementations</li>
</ul>
<h3>Salesforce Commerce Cloud</h3>
<p>Enterprise integration with B2B capabilities:</p>
<ul>
<li><strong>Cartridge Integration:</strong> SFCC-certified cartridge</li>
<li><strong>B2B Support:</strong> Bulk ordering with virtual try-on</li>
<li><strong>Multi-site:</strong> Support for regional brand sites</li>
<li><strong>Timeline:</strong> 2-3 weeks with SFCC partner</li>
</ul>
<h2>Technical Architecture</h2>
<h3>Frontend Integration</h3>
<pre><code>// Example: Initialize virtual try-on widget
const looksy = new LooksyWidget({
  apiKey: 'your-api-key',
  productId: 'product-sku',
  container: '#tryon-container',
  theme: 'light'
});
looksy.init();</code></pre>
<h3>Backend Architecture</h3>
<p>Our enterprise API provides:</p>
<ul>
<li>RESTful endpoints for all operations</li>
<li>Webhook support for real-time updates</li>
<li>99.9% SLA with dedicated support</li>
<li>GDPR and CCPA compliance built-in</li>
</ul>
<h2>Security & Compliance</h2>
<p>Enterprise deployments require:</p>
<ul>
<li><strong>SOC 2 Type II:</strong> Certified data handling</li>
<li><strong>GDPR Compliance:</strong> EU data residency options</li>
<li><strong>Encryption:</strong> AES-256 at rest, TLS 1.3 in transit</li>
<li><strong>Penetration Testing:</strong> Annual third-party audits</li>
</ul>
""",
        "author": "Looksy Engineering",
        "tags": ["enterprise", "integration", "shopify", "magento", "salesforce"],
        "meta_title": "Enterprise Guide: Virtual Try-On Tech Stack Integration",
        "meta_description": "Technical guide for CTOs: integrating virtual try-on with Shopify, Magento, Salesforce Commerce Cloud, and custom platforms.",
        "published_at": "2026-02-09T11:00:00Z",
        "status": "published"
    }
}


@app.get("/")
def root():
    return {
        "service": "Framer CMS Content API",
        "version": "1.0.0",
        "status": "running",
        "posts_count": len(POSTS_DATA)
    }


@app.get("/posts")
def list_posts(status: Optional[str] = None, tag: Optional[str] = None):
    posts = list(POSTS_DATA.values())
    
    if status:
        posts = [p for p in posts if p.get('status') == status]
    if tag:
        posts = [p for p in posts if tag in p.get('tags', [])]
    
    posts.sort(key=lambda x: x.get('published_at', ''), reverse=True)
    return posts


@app.get("/posts/{slug}")
def get_post(slug: str):
    post = POSTS_DATA.get(slug)
    if not post:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.get("/tags")
def list_tags():
    tags = set()
    for post in POSTS_DATA.values():
        tags.update(post.get('tags', []))
    return sorted(list(tags))


if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)