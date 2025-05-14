import axios from '@/configs/axios';

import type { Genre } from '@/types/genre.type';

export const fetchGenres = async (): Promise<Genre[]> => {
	const response = await axios.get('genres/');
	return response.data.result;
};
