export interface Ressurs {
  type: 'lenke' | 'video' | 'notat' | 'oppgave';
  tittel: string;
  url?: string;
  lengde?: string;
}
