export class Api {
  base: string = "http://0.0.0.0";
  token: string = "";

  /**
   * Very basic, rather shitty way of handling authentication.
   * But good enough for this project.
   */
  async signIn(email: string, password: string) {
    const response = await fetch(`${this.base}/sign-in`, {
      headers: { Authenticate: `Basic ${email}:${password}` },
    });

    this.token = (await response.json()).token;

    return this.token;
  }
}
