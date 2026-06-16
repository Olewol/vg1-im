export interface EmneColor {
  color: string;
  bg: string;
}

const COLORS: Record<string, EmneColor> = {
  'teknologiforstaelse': { color: '#4f8cff', bg: 'rgba(79,140,255,.13)' },
  'produksjon-historiefortelling': { color: '#f97316', bg: 'rgba(249,115,22,.13)' },
  'konseptutvikling-programmering': { color: '#10b981', bg: 'rgba(16,185,129,.13)' },
  'tverrfaglig': { color: '#a855f7', bg: 'rgba(168,85,247,.13)' },
  'kompetansemaal': { color: '#ec4899', bg: 'rgba(236,72,153,.13)' },
};

export const EMNE_LIST = Object.keys(COLORS);

export function getEmneColor(emne: string): EmneColor {
  return COLORS[emne] ?? { color: '#6b7280', bg: 'rgba(107,114,128,.13)' };
}

export const FAG_LABELS: Record<string, string> = {
  'teknologiforstaelse': 'Teknologiforståelse',
  'produksjon-historiefortelling': 'Produksjon og historiefortelling',
  'konseptutvikling-programmering': 'Konseptutvikling og programmering',
  'tverrfaglig': 'Tverrfaglig',
  'kompetansemaal': 'Kompetansemål',
};
