import axios from "axios";
import { useForm } from "react-hook-form";
import { Link, useNavigate } from "react-router-dom";

function SignUpPage() {
  const { register, handleSubmit } = useForm();
  const navigate = useNavigate();

  function onSubmit(data) {
    axios.post("http://localhost:8000/api/signup/", data).then(() => {
      navigate("/signin", { replace: true });
    });
  }

  return (
    <div className="flex h-screen items-center justify-center">
      <div>
        <form
          className="flex w-80 flex-col gap-y-6"
          onSubmit={handleSubmit(onSubmit)}
        >
          <div className="flex justify-between gap-x-6">
            <div>
              <label htmlFor="first_name" className="block text-sm font-medium">
                First name
              </label>
              <input
                type="text"
                id="first_name"
                {...register("first_name", { required: true })}
                className="mt-2 w-full rounded-md px-2.5 py-2 text-sm outline-none ring-1 ring-inset ring-gray-300 transition-all focus:ring-2 focus:ring-green-600"
              />
            </div>
            <div>
              <label htmlFor="last_name" className="block text-sm font-medium">
                Last name
              </label>
              <input
                type="text"
                id="last_name"
                {...register("last_name", { required: true })}
                className="mt-2 w-full rounded-md px-2.5 py-2 text-sm outline-none ring-1 ring-inset ring-gray-300 transition-all focus:ring-2 focus:ring-green-600"
              />
            </div>
          </div>
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
          <div>
            <label htmlFor="role" className="block text-sm font-medium">
              Role
            </label>
            <input
              type="text"
              id="role"
              {...register("role", { required: true })}
              className="mt-2 w-full rounded-md px-2.5 py-2 text-sm outline-none ring-1 ring-inset ring-gray-300 transition-all focus:ring-2 focus:ring-green-600"
            />
          </div>
          <button
            type="submit"
            className="w-full rounded-md bg-green-600 py-2 text-sm font-semibold text-white transition-all hover:bg-green-700 active:bg-green-800"
          >
            Sign up
          </button>
        </form>
        <p className="mt-10 block text-center text-sm text-gray-500">
          Already have an account?{" "}
          <Link to="/signin">
            <span className="cursor-pointer font-semibold text-green-600 hover:text-green-700 active:text-green-800">
              Sign in
            </span>
          </Link>
        </p>
      </div>
    </div>
  );
}

export default SignUpPage;
