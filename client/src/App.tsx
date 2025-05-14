import React from 'react';

import Header from '@/components/Header';
import BookList from '@/components/BookList';

const App: React.FC = () => {
	return (
		<div>
			<Header />
			<h1>Welcome to WAKA 🔖</h1>

			<BookList />
		</div>
	);
};

export default App;
