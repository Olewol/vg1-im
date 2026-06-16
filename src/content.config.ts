import { defineCollection, z } from 'astro:content';

const aarsplan = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    skoleaar: z.string(),
    veker: z.array(z.object({
      uke: z.array(z.number()),
      tema: z.string(),
      emne: z.string().nullable().optional(),
      kompetansemaal: z.string().optional().default(''),
      tverrfaglig: z.string().optional().default(''),
      notat: z.array(z.string()).optional().default([]),
      ressurstal: z.number().optional().default(0),
      oppgavetar: z.number().optional().default(0),
      type: z.enum(['undervisning', 'ferie', 'eksamen', 'prosjekt']),
    })),
  }),
});

const emner = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    public: z.boolean().optional().default(true),
    emne: z.string(),
    fag: z.string(),
    uke: z.array(z.number()).optional().default([]),
    kompetansemaal: z.union([z.string(), z.array(z.string())]).optional().default([]),
    kilder: z.array(z.string()).optional().default([]),
    tags: z.array(z.string()).optional().default([]),
    relatert: z.array(z.string()).optional().default([]),
  }),
});

const kompetansemaal = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    public: z.boolean().optional().default(true),
    fag: z.string(),
    kmId: z.string(),
    emne: z.string().default('kompetansemaal'),
  }),
});

export const collections = { aarsplan, emner, kompetansemaal };
