import { FlatList, StyleSheet, Text, View } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useEffect, useState } from 'react';

import axios from '@/configs/axios';

type Category = {
	id: number;
	name: string;
};

const Item = ({ name }: { name: string }) => (
	<View style={styles.item}>
		<Text style={styles.title}>{name}</Text>
	</View>
);

const Genre = () => {
	const [genres, setGenres] = useState<Category[]>([]);

	useEffect(() => {
		fetchGenres();
	}, []);

	const fetchGenres = async () => {
		const res = await axios.get('genres/');
		console.log('API data:', res.data.result);
		setGenres(res.data.result);
	};

	return (
		<FlatList
			data={genres}
			style={{ flex: 1 }}
			contentContainerStyle={{ paddingBottom: 20 }}
			renderItem={({ item }) => <Item name={item.name} />}
			keyExtractor={(item) => item.id.toString()}
		/>
	);
};

const styles = StyleSheet.create({
	item: {
		backgroundColor: '#f9c2ff',
		padding: 20,
		marginVertical: 8,
	},
	title: {
		fontSize: 24,
	},
});

export default Genre;
