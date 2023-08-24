import { createContext, useContext } from "react";

import { User } from "../../../variables/types";

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

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }: AuthProviderProps) => {
    //const [user, setUser] = useState<User | null>(null);
    const user: User | null = null;

    return (
        <AuthContext.Provider value={{ user }}>
            {children}
        </AuthContext.Provider>
    );
}

export const useAuth = () => useContext(AuthContext);

