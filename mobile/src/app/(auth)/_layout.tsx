import React from 'react';
import { Stack } from 'expo-router';

const AuthLayout = () => {
	return (
		<Stack
			screenOptions={{
				headerTransparent: true,
				animation: 'fade',
			}}>
			<Stack.Screen name='login' />
			<Stack.Screen name='register' />
		</Stack>
	);
};

export default AuthLayout;
