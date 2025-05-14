import React from 'react';
import { useQuery } from '@tanstack/react-query';

import Item from './Book';
import { fetchBooks } from '@/services/book.service';

const BookList: React.FC = () => {
	const query = useQuery({ queryKey: ['books'], queryFn: fetchBooks });

	return (
		<div>
			<h2>📚 List Book</h2>
			<ul>
				{query.data?.map((book) => (
					<Item
						key={book.id}
						{...book}
					/>
				))}
			</ul>
		</div>
	);
};

export default BookList;
