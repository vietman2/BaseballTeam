import MyPage from './MyPage';
import { renderWithProviders } from '../../../test-utils/test-utils';

describe('<MyPage />', () => {
  it('should render MyPage', () => {
    renderWithProviders(<MyPage />);
  });
});
