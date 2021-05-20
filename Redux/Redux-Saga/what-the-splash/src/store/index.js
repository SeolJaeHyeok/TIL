import { createStore } from 'redux';
import rootReducer from '../reducers';

const configureStore = () => {
    const store = createStore(
        rootReducer,
        window.__REDUX_DEVTOOLS_EXTENTION__ &&
            window.__REDUX_DEVTOOLS_EXTENSION__(),
    );
    return store;
};

export default configureStore;
