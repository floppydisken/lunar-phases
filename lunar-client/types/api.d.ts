export declare class Api {
    base: string;
    token: string;
    /**
     * Very basic, rather shitty way of handling authentication.
     * But good enough for this project.
     */
    signIn(email: string, password: string): Promise<string>;
}
