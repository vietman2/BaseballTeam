import { createContext, useState, useContext } from "react";

import { User } from "../../variables/types";

// TODO: Finish this

interface AuthContextProps {
    user: User | null;
}

const AuthContext = createContext<AuthContextProps>({
    user: null,
});

interface AuthProviderProps {
    children: React.ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
    const [user, setUser] = useState<User | null>(null);

    return (
        <AuthContext.Provider value={{ user }}>
            {children}
        </AuthContext.Provider>
    );
}

export const useAuth = () => useContext(AuthContext);

