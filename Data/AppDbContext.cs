using Microsoft.EntityFrameworkCore;

public class AppDbContext : DbContext {
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) {

    }

    public DbSet<Accounts>? Accounts { //converts properties into table w/ name Accounts
        get;
        set;
    }
}