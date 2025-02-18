import { type RouteConfig, index, route, layout } from "@react-router/dev/routes";

// theninitial route of our app
export default [
    index("routes/home.tsx"),
    route("about", "routes/about.tsx"),
    // routes that accept parameters
    route("post/:postId", "routes/post.tsx"),

    // // nested routes
    // route("dashboard", "routes/dashboard.tsx", [
    //     route("finances", "routes/finances.tsx"),
    //     route("personal", "routes/personal.tsx")
    // ]),


    // layout routes
    layout("routes/dashboard.tsx", [
        route("finances", "routes/finances.tsx"),
        route("personal", "routes/personal.tsx")
    ])


] satisfies RouteConfig;

// routing is configured here
// 