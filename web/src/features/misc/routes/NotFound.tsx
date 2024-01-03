import { Box, Typography } from '@mui/material';

import { styles } from './styles';
export const NotFound = () => {
  return (
    <Box sx={styles.notFoundBox}>
      <Typography variant="h1">404</Typography>
    </Box>
  );
};
