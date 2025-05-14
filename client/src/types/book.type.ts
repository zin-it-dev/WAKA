import type { Base } from './base.type';

export type Book = Base & {
	title: string;
	price: number;
};
