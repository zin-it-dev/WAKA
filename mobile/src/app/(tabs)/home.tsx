import { Text, StyleSheet } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

import Genre from '@/components/Genre';

const Home = () => {
	return (
		<SafeAreaView style={styles.container}>
			<Text>Home</Text>
			<Genre />
		</SafeAreaView>
	);
};

const styles = StyleSheet.create({
	container: {
		flex: 1,
		padding: 16,
	},
});

export default Home;
