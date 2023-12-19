import { ReactElement } from 'react';
import { render } from '@testing-library/react-native';
import { Provider } from 'react-redux';

import store from '../store/store';

const AllTheProviders = ({ children }: { children: ReactElement }) => {
  return <Provider store={store}>{children}</Provider>;
};

const customRender = (ui: ReactElement, options?: any) =>
    render(ui, { wrapper: AllTheProviders, ...options });

export * from '@testing-library/react-native';
export { customRender as render };