import { createBrowserRouter } from "react-router-dom";

import ProtectedRoute from "./components/ProtectedRoute";

import HomePage from "./pages/HomePage";
import SignInPage from "./pages/SignInPage";
import SignUpPage from "./pages/SignUpPage";

// Patron //
import CartList from "./roles/patron/CartList";
import CartDetail from "./roles/patron/CartDetail";
import Checkout from "./roles/patron/Checkout";
import OrderList from "./roles/patron/OrderList";
import OrderDetail from "./roles/patron/OrderDetail";
import RestaurantList from "./roles/patron/RestaurantList";
import RestaurantDetail from "./roles/patron/RestaurantDetail";

// Runner //
import ManageOrderList from "./roles/runner/ManageOrderList";
import ManageOrderDetail from "./roles/runner/ManageOrderDetail";

// Vendor //
import ManageRestaurantList from "./roles/vendor/ManageRestaurantList";
import ManageRestaurantDetail from "./roles/vendor/ManageRestaurantDetail";

const browserRouter = createBrowserRouter([
  {
    path: "/",
    element: (
      <ProtectedRoute>
        <HomePage />
      </ProtectedRoute>
    ),
    children: [
      {
        path: "carts",
        element: <CartList />,
        children: [
          {
            path: ":cartId",
            element: <CartDetail />,
          },
        ],
      },

      {
        path: "orders",
        element: <OrderList />,
        children: [
          {
            path: ":orderId",
            element: <OrderDetail />,
          },
        ],
      },

      {
        path: "restaurants",
        element: <RestaurantList />,
        children: [
          {
            path: ":restaurantId",
            element: <RestaurantDetail />,
            children: [
              {
                path: "checkout",
                element: <Checkout />,
              },
            ],
          },
        ],
      },

      {
        path: "manage-orders",
        element: <ManageOrderList />,
        children: [
          {
            path: ":orderId",
            element: <ManageOrderDetail />,
          },
        ],
      },

      {
        path: "manage-restaurants",
        element: <ManageRestaurantList />,
        children: [
          {
            path: ":restaurantId",
            element: <ManageRestaurantDetail />,
          },
        ],
      },
    ],
  },
  { path: "/signin", element: <SignInPage /> },
  { path: "/signup", element: <SignUpPage /> },
]);

export default browserRouter;
