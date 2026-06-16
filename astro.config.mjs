// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import mermaid from 'astro-mermaid';
import expressiveCode from 'astro-expressive-code';
import sitemap from '@astrojs/sitemap';
import mdx from '@astrojs/mdx';

const BASE = '/vg1-im';

export default defineConfig({
  site: 'https://Olewol.github.io/vg1-im',
  base: BASE,
  integrations: [
    tailwind(),
    mermaid(),
    expressiveCode(),
    sitemap(),
    mdx(),
  ],
  markdown: {
    rehypePlugins: [
      ['rehype-external-links', { target: '_blank', rel: ['noopener', 'noreferrer'] }]
    ],
  },
});
