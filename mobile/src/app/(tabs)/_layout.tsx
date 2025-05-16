import { Tabs } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import React from 'react';

const TabsLayout = () => {
	return (
		<Tabs>
			<Tabs.Screen
				name='home'
				options={{
					title: 'Home',
					tabBarIcon: ({ color }) => (
						<Ionicons
							name='home'
							color={color}
							size={24}
						/>
					),
				}}
			/>
			<Tabs.Screen
				name='search'
				options={{
					title: 'Search',
					tabBarIcon: ({ color }) => (
						<Ionicons
							name='search'
							color={color}
							size={24}
						/>
					),
				}}
			/>
			<Tabs.Screen
				name='cart'
				options={{
					title: 'Cart',
					tabBarIcon: ({ color }) => (
						<Ionicons
							name='cart'
							color={color}
							size={24}
						/>
					),
				}}
			/>
		</Tabs>
	);
};

export default TabsLayout;
