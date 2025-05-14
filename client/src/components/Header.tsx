import { useQuery } from '@tanstack/react-query';
import React from 'react';

import { fetchGenres } from '@/services/genre.service';

const Header: React.FC = () => {
	const query = useQuery({ queryKey: ['genres'], queryFn: fetchGenres });

	console.log(query.data);

	return (
		<div>
			<ul>
				{query.data?.map((genre) => (
					<li key={genre.id}>{genre.name}</li>
				))}
			</ul>
		</div>
	);
};

export default Header;
