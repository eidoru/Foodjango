import { useContext } from "react";
import { AuthContext } from "../contexts/AuthContext";

function useAuth() {
  const { token, setToken } = useContext(AuthContext);
  return { token, setToken };
}

export { useAuth };
