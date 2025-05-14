import React from 'react';

import type { Book } from '@/types/book.type';

const Item: React.FC<Book> = (item: Book) => {
	return (
		<li>
			<strong>{item.title}</strong> - 💵 {item.price}$
			{item.isActive ? ' ✅' : ' ❌'}
		</li>
	);
};

export default Item;
