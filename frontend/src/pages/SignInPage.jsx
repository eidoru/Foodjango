import axios from "axios";
import { useForm } from "react-hook-form";
import { useAuth } from "../hooks/useAuth";
import { Link, useNavigate } from "react-router-dom";

function SignInPage() {
  const { register, handleSubmit } = useForm();
  const { setToken } = useAuth();
  const navigate = useNavigate();

  function onSubmit(data) {
    axios.post("http://localhost:8000/api/signin/", data).then((response) => {
      if (response.data.status === true) {
        setToken(response.data.token);
        navigate("/", { replace: true });
      }
    });
  }

  return (
    <div className="flex h-screen items-center justify-center">
      <div>
        <form
          className="flex w-80 flex-col gap-y-8"
          onSubmit={handleSubmit(onSubmit)}
        >
          <div>
            <label htmlFor="username" className="block text-sm font-medium">
              Username
            </label>
            <input
              type="text"
              id="username"
              {...register("username", { required: true })}
              className="mt-2 w-full rounded-md px-2.5 py-2 text-sm outline-none ring-1 ring-inset ring-gray-300 transition-all focus:ring-2 focus:ring-green-600"
            />
          </div>
          <div>
            <label htmlFor="password" className="block text-sm font-medium">
              Password
            </label>
            <input
              type="password"
              id="password"
              {...register("password", { required: true })}
              className="mt-2 w-full rounded-md px-2.5 py-2 text-sm outline-none ring-1 ring-inset ring-gray-300 transition-all focus:ring-2 focus:ring-green-600"
            />
          </div>
          <button
            type="submit"
            className="w-full rounded-md bg-green-600 py-2 text-sm font-semibold text-white transition-all hover:bg-green-700 active:bg-green-800"
          >
            Sign in
          </button>
        </form>
        <p className="mt-10 block text-center text-sm text-gray-500">
          Don&apos;t have an account?{" "}
          <Link to="/signup">
            <span className="cursor-pointer font-semibold text-green-600 hover:text-green-700 active:text-green-800">
              Sign up
            </span>
          </Link>
        </p>
      </div>
    </div>
  );
}

export default SignInPage;
