import { useRoutes } from 'react-router-dom';

import { NotFound } from '@/features/misc';

import { publicRoutes } from './public';

export const AppRoutes = () => {
  const commonRoutes = [{ path: '/*', element: <NotFound /> }];

  const element = useRoutes([...commonRoutes, ...publicRoutes]);

  return <>{element}</>;
};
