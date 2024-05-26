import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";

function ProtectedRoute({ children }) {
  const navigate = useNavigate();
  const { token } = useAuth();

  useEffect(() => {
    if (token === null || token === "null") {
      console.log("Lol");
      navigate("/signin", { replace: true });
    }
  }, [navigate, token]);

  return children;
}

export default ProtectedRoute;
