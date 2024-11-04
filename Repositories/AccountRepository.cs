using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using DbProject1.Models;
using DbProject1.Data;
using DbProject1.Repositories;

namespace DbProject1.Repositories
{
    // Implementation of the Account repository
    public class AccountRepository : IAccountRepository
    {
        private readonly AppDbContext _context;

        public AccountRepository(AppDbContext context)
        {
            _context = context;
        }

        public async Task<Accounts> GetAccountByIdAsync(int id)
        {
            var account = await _context.Accounts.FindAsync(id);
            return account ?? throw new KeyNotFoundException($"No account found with ID {id}");
        }

        public async Task<IEnumerable<Accounts>> GetAllAccountsAsync()
        {
            return await _context.Accounts.ToListAsync();
        }

        public async Task AddAccountAsync(Accounts account)
        {
            if (account == null)
            {
                throw new ArgumentNullException(nameof(account), "Account cannot be null");
            }

            _context.Accounts.Add(account);
            await _context.SaveChangesAsync();
        }

        public async Task UpdateAccountAsync(Accounts account)
        {
            if (account == null)
            {
                throw new ArgumentNullException(nameof(account), "Account cannot be null");
            }

            // Ensure that the account exists in the database before updating
            var existingAccount = await _context.Accounts.FindAsync(account.HireeID);
            if (existingAccount == null)
            {
                throw new KeyNotFoundException($"No account found with ID {account.HireeID}");
            }

            _context.Entry(existingAccount).CurrentValues.SetValues(account);
            await _context.SaveChangesAsync();
        }

        public async Task DeleteAccountAsync(int id)
        {
            var account = await _context.Accounts.FindAsync(id);
            if (account != null)
            {
                _context.Accounts.Remove(account);
                await _context.SaveChangesAsync();
            }
            else
            {
                throw new KeyNotFoundException($"No account found with ID {id}");
            }
        }
    }
}
