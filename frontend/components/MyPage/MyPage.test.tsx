import { screen } from '@testing-library/react-native';

import MyPage from './MyPage';
import { render } from '../../test-utils/test-utils';

describe('<MyPage />', () => {
  it('should render MyPage', () => {
    render(<MyPage />);

    expect(screen.getByText('마이페이지 화면'));
  });

  it('should fail the test', () => {
    render(<MyPage />);

    expect(screen.getByText('마이페이지 화면2'));
  });
});