import { ReactElement } from 'react';

import { Landing } from '@/features/misc';

export interface PublicRouteProps {
  path: string;
  element: ReactElement;
}

export const publicRoutes: PublicRouteProps[] = [
  {
    path: '/',
    element: <Landing />,
  },
];
