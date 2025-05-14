import type { Book } from '@/types/book.type';
import axios from '@/configs/axios';

export const fetchBooks = async (): Promise<Book[]> => {
	const response = await axios.get('books');
	return response.data.result;
};
